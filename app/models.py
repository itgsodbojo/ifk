from pony.orm import *
from app import db



class Member(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    phone = Optional(str, nullable=True)
    particpants = Set("Particpant")


class Section(db.Entity):
    sectioncode = PrimaryKey(str)
    name = Required(str)
    leader = Required(int)
    particpants = Set("Particpant")


class Particpant(db.Entity):
    member = Required(Member)
    section = Required(Section)
    PrimaryKey(member, section)


