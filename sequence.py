from sqlalchemy import Column, String, Integer, Date, Table

from base import Base

"""
seq table

Will connect to struc table - one to many as
a sequence can have multiple structures

"""

class Seq(Base):
	__tablename__ = 'seq'

	id = Column(Integer, primary_key=True)
	uniprot = Column(String)
	sequence = Column(String)
	name = Column(String)

	def __init__(self, uniprot, sequence, name):
		self.uniprot = uniprot
		self.sequence = sequence
		self.name = name