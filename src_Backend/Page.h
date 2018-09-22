#include<string>
#include<queue>
#include<iostream>
#include<fstream>
#include"Widget_Collection.h"
#ifndef PAGE_H
#define PAGE_H

using namespace std;

class Page
{
private:
	string _data;
	string _basic_import;
	string _extra_import;
	string _activity_prefix;
	string _activity_postfix;
	string _activity_PageGet;
	string _activity_SetUI;
	string _page_name;
	string _package_name;
	bool _if_gen_stdfunc;
	queue<string> _functions;
	bool *_exist_record;
	queue<string>* _ids;


	void init_fixed_info();
	void put_package_name();
	void put_import();
	void put_activity();
	void put_activity_prefix();
	void put_activity_postfix();
	void put_activity_content();
	void put_activity__widget_declaration();
	void put_activity__PageGet();
	void put_activity__setUI();
	void put_activity__loadControl();
	void put_activity__widget_function();
	void gen_func_content(string func_name);
	void put_activity__onClick();
public:
	Page(const char* page_name, const char* package_name, bool if_gen_stdfunc);
	void set_page_name(const char* page_name);
	void set_package_name(const char* package_name);
	void add_func(const char* func);
	void gen_data();
	void save(const char* filename);
	void print_button();
	void set_extra_import(string import_data);
	bool* get_exist_record_pointer();
	queue<string>* get_ids_pointer();
};

#endif // PAGE_H
