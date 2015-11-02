# coding: utf-8
import string
from random import choice
from model_mommy import generators

my_string = '''
Lorem ipsum dolor sit amet, vel paulo pertinax ei, mei alia volutpat ei. Ea delenit expetenda incorrupte mea. Ut denique iudicabit nec. At vis soleat definiebas.

Ut dicam quaeque eligendi vix, vis no copiosae consequuntur. Tale regione persecuti cu mea, vel omnis dolorem hendrerit et. Suas mucius signiferumque ex vim, te deleniti gloriatur definitiones sit. Nec ad decore pertinax, ut per sapientem euripidis reprehendunt, oportere definitionem ad vix. Est cu case rebum iuvaret, eum in partem signiferumque. Sea at nulla delectus, qui admodum periculis ex.

Vim te choro integre, vide congue eos cu. Aeque noluisse ad qui. Ex dicta minimum pro, sit et appetere nominati platonem, cum cu eripuit maluisset. Inermis ceteros vivendum et vim. No est evertitur abhorreant, congue lobortis aliquando sit ad, est ad quem accusamus. Eum accusamus persecuti ne, usu cu erat platonem, no decore principes per.

Munere mollis scriptorem eu pro, saepe noster aperiam at sed, tollit scaevola appellantur eum at. Qui agam sale augue te, ea quem molestie pericula vix. Est sint vocent id, sonet copiosae petentium cu has. Tation maiorum fabellas an pro. Usu illum voluptaria consectetuer eu, adipisci suscipiantur per at, petentium constituam nam ad. An sonet facilisis cum.

An habeo populo scripta eos, ad invidunt recusabo consequuntur mei. Vidit etiam assentior mea eu, te eum primis verterem. Sea salutatus quaerendum at, eu veritus quaerendum accommodare sea. Mea ornatus senserit ad, cum ea ferri viderer. Legere volutpat euripidis ea usu, eum in ubique timeam, ea meis viderer recteque nec. Et usu putant inermis voluptua, eu mea novum deleniti euripidis.
'''


def generator_string_by_range(type_string='letters', min=6, max=12):
    max_length = choice(range(min, max+1))
    if type_string == 'lowercase':
        return str(''.join(choice(string.ascii_lowercase) for i in range(max_length)))
    elif type_string == 'uppercase':
        return str(''.join(choice(string.ascii_uppercase) for i in range(max_length)))
    else:
        return str(''.join(choice(string.ascii_letters) for i in range(max_length)))
