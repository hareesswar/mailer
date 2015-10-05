#from campaign import CampaignFactory

import argparse

import os

def console_main():
		
	current=os.getcwd()

	parser = argparse.ArgumentParser(description='Command line mail app \n Choose Type: \n smartSend: pathname which has the required files \n noobSend: pass individual')
	parser.add_argument('-s','--subject', help='Subject of email')
	parser.add_argument('-r','--receivers',nargs='+',help='Receivers List in qoutes separated by space')
	parser.add_argument('-t','--template',help="template file" )
	parser.add_argument('-g','--globalVar',help="global variable file")
	parser.add_argument('-sm','--smartSend',help="path for smart send" ,default="NULL")

	args = vars(parser.parse_args())

	smartSend=args['smartSend']

	def smartSendFun():

		subject=smartSend+"\subject.txt"
		receiversList=smartSend+"\mailinglist.ml"
		template=smartSend+"\\template.mmtmpl"
		globalVar=smartSend+"\globals.mvar"
		return [subject,receiversList,template,globalVar]

	def noobSend():
		if args['subject']:
			subject=args['subject']
		else:
			subject=current+"\subject.txt"
		if args['receivers']:
			receiversList=args['receivers']
		else:
			receiversList=current+"\mailinglist.ml"
		if args['template']:
			template=args['template']
		else:
			template=current+"\\template.mmtmpl"	
		if args['globalVar']:
			globalVar=args['globalVar']
		else:
			globalVar=current+"\globals.mvar"
		return [subject,receiversList,template,globalVar]
	

	if smartSend=="NULL":
		print noobSend() 
		#camobj=CampaignFactory( *noobSend() )
	else:
		print smartSendFun() 
		#camobj = CampaignFactory( *smartSendFun() )

	#camobj.send()	