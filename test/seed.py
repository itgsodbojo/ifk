
import sys
import os

sys.path.append("../")

try:
    os.remove("../app/ifk.db")
except:
    pass


from pony.orm import db_session
from app.models import Member,Section,Particpant


# create new member Bosse
with db_session:
    bosse = Member(name="bosse",phone="0702191971")


#create section boxning and set the bosse to be leader
with db_session:
    boxning = Section(sectioncode="A",name= "boxning", leader = bosse.id)

# create new members
with db_session:
    hasse = Member(name="hasse",phone="097551082")
    lasse = Member(name="hasse",phone="097030308")

# add new members to boxning
with db_session:
    newparticpant=Particpant(member=hasse.id,section=boxning.sectioncode)
    newparticpant=Particpant(member=lasse.id,section=boxning.sectioncode)