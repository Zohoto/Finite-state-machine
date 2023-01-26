import translit as tr
import lexical as lex
import check_syntax as ch_syn


data = tr.translit()
print(data)

lexic = lex.lexical(data)
print(lexic)

ch_syn.check_syntax(lexic)