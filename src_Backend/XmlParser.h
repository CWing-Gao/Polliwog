#ifndef XMLPARSER_H
#define XMLPARSER_H

#include<iostream>
#include"Page.h"
#include"tinyxml/tinystr.h"
#include"tinyxml/tinyxml.h"
#include"Widget_Collection.h"
#include<windows.h>
#include<string>

using namespace std;

class XmlParser
{
private:
	string _filename;
	Page* _bind_page;
	TiXmlDocument _doc;
	int _init;
	void load_file();
	void traverse(TiXmlElement* element);
	void record_exist(int index);
	void record_ids(int index, const char* id);
	string gen_import();
	void import2page();
	void func2page();
	bool *_exist_record;
	queue<string>* _ids;
public:
	XmlParser(const char* filename);
	void set_filename(const char* filename);
	void bind_page(Page* bindpage);
	void parse2Page();
};

#endif // XMLPARSER_H
