from base import Session, engine, Base

from sequence import Seq
from struc import Struc 

import urllib.parse
import urllib.request

import xml.etree.ElementTree as ET

def uniprot_info(uniprotId):
	"""
	Use uniprot API to get list of PDB files and chains
	"""
	pdbs_chains = [] # list of dicts. For Struc table

	uni_info = {
	"seq":"",
	"name":"",
	"uniprot":uniprotId
	} # dict with seq, name, id etc. for Seq table

	url = 'https://www.uniprot.org/uniprot/'

	params = {
	'query': 'accession:'+uniprotId,
	'format': 'xml',
	}

	data = urllib.parse.urlencode(params)
	data = data.encode('utf-8')
	req = urllib.request.Request(url, data)
	with urllib.request.urlopen(req) as f:
		response = f.read()
		root = ET.fromstring(response)

		for child in root[0]:
			if(child.tag.endswith('sequence')):
				uni_info["seq"] = child.text
			elif(child.tag.endswith('name')):
				uni_info["name"] = child.text
			elif(child.tag.endswith("dbReference")):
				if(child.attrib["type"] == "PDB"):
					pdbid = child.attrib["id"]
					pdbres = None # default if NMR
					for grandchild in child:
						if(grandchild.attrib["type"]=="method"):
							pdbmethod = grandchild.attrib["value"]
						elif(grandchild.attrib["type"]=="resolution"):
							pdbres = float(grandchild.attrib["value"][0:-2])
						elif(grandchild.attrib["type"]=="chains"):
							pdbchains = grandchild.attrib["value"]
					# now need to process the chains then create dicts
					# to be put in pdbs_chains list
					pdbchains = pdbchains.split("=")[0]
					pdbchains = pdbchains.split("/")
					for c in pdbchains:
						tmp = {
						"id": pdbid,
						"chain": c,
						"res" : pdbres,
						"method": pdbmethod
						}
						pdbs_chains.append(tmp)
	if(len(pdbs_chains)==0):
		return(False, False)
	else:
		return(uni_info, pdbs_chains)

def add_single_entry(uniprot_id):
	Base.metadata.create_all(engine)

	session = Session()

	# user provides a uniprot ID. We need to get info using uniprot API

	uni_info, pdbs_chains = uniprot_info(uniprot_id)

	if(uni_info and pdbs_chains):
		# create seq data
		seq_data = Seq(uni_info["uniprot"], uni_info["seq"], uni_info["name"])

		chain_data = []
		for c in pdbs_chains:
			chain_data.append(Struc(c["id"], c["chain"], c["method"], c["res"], seq_data))

		session.add(seq_data)

		for c in chain_data:
			session.add(c)

		session.commit()
		session.close()

		print(f'{uniprot_id} - {str(len(pdbs_chains))} PDB chains added to Database.')


	else:
		print(f'{uniprot_id} does not have any associated PDB structures.')




