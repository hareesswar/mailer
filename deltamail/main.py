#from campaign import CampaignFactory

import os.path

import argparse

import os

def console_main():
		
	current=os.getcwd()

	parser = argparse.ArgumentParser(description='Command line mail app \n Choose Type: \n smartSend: pathname which has the required files \n noobSend: pass individual')
	parser.add_argument('-s','--subject', help='Subject of email')
	parser.add_argument('-r','--receivers',nargs='+',help='Receivers List in qoutes separated by space')
	parser.add_argument('-t','--template',help="template file" )
	parser.add_argument('-g','--global_var',help="global variable file")
	parser.add_argument('-sm','--smart_send',help="path for smart send" ,default="NULL")

	args = vars(parser.parse_args())

	smart_send=args['smart_send']

	def smart_send_fun():

		subject=os.path.join(smart_send,"subject.txt")
		receivers_list=os.path.join(smart_send,"mailinglist.ml")
		template=os.path.join(smart_send,"template.mmtmpl")
		global_var=os.path.join(smart_send,"globals.mvar")
		return [subject,receivers_list,template,global_var]

	def noob_send():
		if args['subject']:
			subject=args['subject']
		else:
			subject=os.path.join(current,"subject.txt")
		if args['receivers']:
			receivers_list=args['receivers']
		else:
			receivers_list=os.path.join(current,"mailinglist.ml")
		if args['template']:
			template=args['template']
		else:
			template=os.path.join(current,"template.mmtmpl")	
		if args['global_var']:
			global_var=args['global_var']
		else:
			global_var=os.path.join(current,"globals.mvar")
		return [subject,receivers_list,template,global_var]
	

	if smart_send=="NULL":
		print noob_send() 
		#camobj=CampaignFactory( *noob_send() )
	else:
		print smart_send_fun() 
		#camobj = CampaignFactory( *smart_send_fun() )
	#camobj.send()	