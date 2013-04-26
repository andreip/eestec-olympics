#!/usr/bin/env python
from xml.dom import minidom

from polls.models import Entry
from polls.models import Publisher
from polls.models import Published

from polls.models import Place
#export DJANGO_SETTINGS_MODULE=eestec_site.settings
xmldoc = minidom.parse('library_sample.xml')

root = xmldoc.documentElement
print root
#atr = root.getAttributeNode('lang')
itemlist = xmldoc.getElementsByTagName('topic')
aux = xmldoc.getElementsByTagName('title')
descr = xmldoc.getElementsByTagName('shortdesc')

name_author = xmldoc.getElementsByTagName('author')

isbn_list = xmldoc.getElementsByTagName('isbn')

file_list = xmldoc.getElementsByTagName('file')
body_list = xmldoc.getElementsByTagName('body')
parag = xmldoc.getElementsByTagName('p')
for i in range(len(itemlist)):
	print "printing value of nodes"
	print itemlist[i].firstChild.nodeValue
	lang_aux = itemlist[i].attributes['lang'].value
	print lang_aux
	id_aux = itemlist[i].attributes['id'].value
	print id_aux
	type_aux = itemlist[i].attributes['type'].value
	print type_aux
	format_aux = itemlist[i].attributes['format'].value
	print format_aux
	platform_aux = itemlist[i].attributes['platform'].value
	print platform_aux
	platform_aux_name = itemlist[i].attributes['platformName'].value
	print platform_aux_name
	publ_aux = aux[0].attributes['publisher'].value
	print publ_aux
	publ_year_aux = aux[0].attributes['year'].value
	print publ_year_aux
	title = aux[0].firstChild.nodeValue
	print title
	descr_aux = descr[i].firstChild.nodeValue
	print descr_aux
	author = name_author[i].firstChild.nodeValue
	print author
	if len(isbn_list[i].attributes) > 0 :
		isbn_type = isbn_list[i].attributes['standard'].value
	print isbn_type
	#print "lennnn is "+ str(len(isbn_list[i]))
	if len(isbn_list[i].childNodes) > 0:
		isbn = isbn_list[i].firstChild.nodeValue
	print isbn
	file_name = file_list[i].firstChild.nodeValue
	print file_name
	p_id = parag[i].attributes['audience'].value
	print p_id
	p_cont = parag[i].firstChild.nodeValue
	print p_cont	
	c = Publisher(name=title)
	c.save()
	d = Published(publisher=c,year=publ_year_aux,value=publ_aux)
	d.save()
	e = Place(name="Poli")
	e.save()
	b = Entry(format_type=format_aux,language=lang_aux,author=author,file_name=file_name,audience=p_id,body=p_cont,isbn_value=isbn,isbn_type=isbn_type,descr=descr_aux,platformName=platform_aux_name,platform=platform_aux,identif=id_aux,file_type=type_aux,published=d)
	b.save()

