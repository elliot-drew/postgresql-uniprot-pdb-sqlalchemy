from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from base import Base

"""
Struc table

Can have many struc entries per sequence.

Struc entry has pdbid AND chain -> sequence.

"""

class Struc(Base):
	__tablename__ = "struc"

	id = Column(Integer, primary_key=True)
	pdbid = Column(String)
	chain = Column(String)
	method = Column(String)
	resolution = Column(Float)
	seq_id = Column(Integer, ForeignKey('seq.id'))
	seq = relationship("Seq", backref="struc")

	def __init__(self, pdbid, chain, method, resolution, seq):
		self.pdbid = pdbid
		self.chain = chain
		self.method = method
		self.resolution = resolution
		self.seq = seq
