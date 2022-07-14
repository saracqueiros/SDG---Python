from ctypes import sizeof
from distutils.command.build import build
from re import S, X
from tkinter import FALSE
from unicodedata import decimal
from lark import Lark,Token
from lark.tree import pydot__tree_to_png
from lark.visitors import Interpreter
from html import finalData
from sys import argv
import copy
import graphviz
from sdg import *


#Testar:
#: > result.html | python LPIS2_graph.py exemplo.txt >> result.html 

class MyInterpreter (Interpreter):

  def __init__(self):
    self.prev_node = list()
    self.prev_node.append('Entry')
    sdg.node('Entry', fontcolor='black', color='black')
    return 

  def start(self, tree):
    self.visit(tree.children[0])
    return finalData()
    
  def code(self, tree):
    #code: (variaveis | funcao | cond | output | ciclos)+ 
    for child in tree.children[0:]:
      self.visit(child)
        
  def variaveis(self, tree):
    #variaveis: (declaracoes | atribuicoes) PV 
    return self.visit(tree.children[0])

  def obtainNode(self, elems):
    node = ''
    for elem in elems:
      if isinstance(elem, Token):
        node = node + elem + ' '
      else :
        for i in elem:
            if not isinstance(i, Token):
              for ii in i:
                  node = node + ii 
            else:
               node = node + i + ' '
    return node


  def declaracoes(self, tree):
    #declaracoes: decint | decstring | decdict | declist | decconj | dectuplos | decfloat | decinput 
    dec = self.visit(tree.children[0])
    #formar a string necessária, meter num nodo e ligar o nodo ao anterior 
    node = self.obtainNode(dec)
    sdg.node(node, fontcolor='blue', color='blue')
    sdg.edge(self.prev_node[-1], node)
    

    return
 

  def atribuicoes(self, tree):
    # atribuicoes: WORD IGUAL (var | operacao | input |lista | dicionario) 
    var = self.visit_children(tree)
    node = self.obtainNode(var)
    sdg.node(node, fontcolor='green', color='green')
    sdg.edge(self.prev_node[-1], node)
    return 
  

  def input(self, tree):
    #input: INPUTW PE PD 
    self.visit_children(tree)
    node = 'input()'
    #buildNodeIO(self, r, g)
    return node

  def output(self, tree):
    #output: OUTPUTW PE ESCAPED_STRING PD PV
    self.visit_children(tree)
    return 

'''

  def ciclos(self, tree):
    #(whilee | forr | dowhile) PV
    self.visit(tree.children[0])
    return  

  def whilee(self, tree):
    #WHILEW PE condicao PD CE code? CD 
    cndt = self.visit(tree.children[2])    
    return 

  def cond(self, tree):
    #cond: IFW PE condicao PD CE code? CD else? PV
    return 
  
  def condicao(self, tree):
    #condicao: var ((II|MAIOR|MENOR|DIF|E|OU) var)?
    cndt = "("
    return cndt

  def forr(self, tree):
    #forr: FORW PE variaveis condicao PV atribuicoes PD CE code? CD  
    self.visit(tree.children[2])
    return  
  
  def dowhile (self, tree):
    #dowhile: DOW CE code? CD WHILEW PE condicao PD PV
    cndt  = self.visit(tree.children[len(tree.children)-2]) ##condição 
    for elem in tree.children:
      if not isinstance(elem, Token) and  elem.data== 'code':
        self.visit(elem) 
    


  def elsee(self,tree):
    #elsee: ELSEW CE code CD
    for elem in tree.children:
      if not isinstance(elem, Token):
        self.visit(elem)
      
 
  def funcao(self, tree):
    #DEFW WORD PE args PD CE code? return? CD 
    for elem in tree.children[:6]:
      if not isinstance(elem, Token):
        self.visit(elem)
    if not isinstance(tree.children[6], Token):
      if tree.children[6].data == 'code':
        self.visit(tree.children[6])

'''      
    
  
  

## Primeiro precisamos da GIC
grammar = '''
start: code
code: (variaveis | funcao | cond | output | ciclos)+ 

variaveis: (declaracoes | atribuicoes) PV 
declaracoes: decint | decstring | decdict | declist | decconj | dectuplos | decfloat | decinput
decint : INTW WORD (IGUAL (INT | operacao))? 
  operacao : (NUMBER|WORD) ((SUM | SUB | MUL | DIV | MOD) (NUMBER|WORD))+
decstring : STRINGW WORD (IGUAL (ESCAPED_STRING|input))? 
decdict : DICTW WORD (IGUAL DICTW PE PD)? 
declist : INTW WORD (PRE NUMBER? PRD)+ (IGUAL (content | ultracontent))?
  content : CE (INT (VIR INT)*)* CD
  ultracontent: CE (content (VIR content)*)* CD
decconj: CONJW  WORD (IGUAL CE (ESCAPED_STRING (VIR ESCAPED_STRING)*)? CD )* 
dectuplos: TUPLEW WORD (IGUAL PE var (VIR var)+ PD)* 
  var: INT | WORD | ESCAPED_STRING | FLOAT 
decfloat: FLOATW WORD (IGUAL FLOAT)* 
decinput: STRINGW IGUAL input

atribuicoes: WORD IGUAL (var | operacao | input |lista | dicionario) 
  input: INPUTW PE PD 
  lista: WORD (PRE INT PRD)+
  dicionario: CE ESCAPED_STRING DP (INT | WORD)(VIR ESCAPED_STRING DP (INT | WORD))* CD 

funcao: DEFW WORD PE args PD CE code? return? CD 
  args: (types WORD VIR)* types WORD 
  types: (STRINGW |DICTW |INTW | TUPLEW| FLOATW| CONJW)
  return: RETURNW (WORD VIR)* WORD
  DEFW: "def"
  RETURNW: "return" 

cond: IFW PE condicao PD CE code? CD elsee? PV
  condicao: var ((II|MAIOR|MENOR|DIF|E|OU) var)?
  elsee: ELSEW CE code? CD
  ELSEW: "else"

output: OUTPUTW PE (ESCAPED_STRING|WORD) PD PV

ciclos: (whilee | forr | dowhile) PV
whilee: WHILEW PE condicao PD CE code? CD 
forr: FORW PE variaveis condicao PV atribuicoes PD CE code? CD 
dowhile: DOW CE code? CD WHILEW PE condicao PD 

DP: ":"
INTW: "int"
INPUTW: "input"
OUTPUTW: "print"
STRINGW: "string"
DICTW: "dict"
CONJW: "conj"
TUPLEW: "tuple"
FLOATW: "float"
WHILEW: "while"
DOW: "do"
IFW: "if"
FORW: "for"
PE:"("
PRE:"["
PRD: "]"
PD:")"
CE:"{"
CD:"}"
PV:";"
VIR:","
SUM: "+"
SUB: "-"
MUL: "*"
DIV: "/"
MOD: "%"
II: "=="
MAIOR: ">"
MENOR: "<"
DIF: "!="
E: "&&"
OU: "||"
IGUAL:"="
WORD: "a".."z"("a".."z"|"0".."9")*


%import common.WS
%import common.INT
%import common.FLOAT
%import common.ESCAPED_STRING
%import common.NUMBER

%ignore WS
'''

f = open(argv[1], "r")
sdg = graphviz.Digraph('sdg', format='png')
sdg.graph_attr['rankdir'] = 'TB'

linhas = f.read()
p = Lark(grammar, propagate_positions = True) 
parse_tree = p.parse(linhas)
#print(parse_tree.pretty())
data = MyInterpreter().visit(parse_tree)
sdg.render(directory='doctest-output', view=False)  
print(data)







