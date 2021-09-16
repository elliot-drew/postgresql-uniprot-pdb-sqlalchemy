
"""
some example queries for my reference if i forget them
"""

from base import Session, engine, Base

from sequence import Seq
from struc import Struc 

session = Session()

sequences = session.query(Seq).all() # to get all sequences
structures = session.query(Struc).all() # to get all structures

# get all sequences entries longer than 500 residues
sequences_500 = session.query(Seq).filter(func.Length(Seq.sequence) > 500).all()

# get the pdbids of all sequences longer than 500 residues
structures_500 = session.query(Struc.pdbids) \
	.join(Seq, Struc.seq) \
	.filter(func.Length(Seq.sequence)>500) \
	.all()

# get uniprotids that have NMR structures

sequences_NMR  = session.query(Seq.uniprot, Struc.method) \
	.join(Struc.seq) \
	.filter(Struc.method == "NMR")
	.all()
