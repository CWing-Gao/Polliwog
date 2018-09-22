#pragma comment( linker, "/subsystem:windows /entry:mainCRTStartup" )
#include<iostream>
#include"Page.h"
#include"XmlParser.h"
#include"Widget_Collection.h"
#include<cstdlib>

using namespace std;

int main(int argc,char** argv) {
	if (argc != 6)exit(-1);
	string ifile(argv[1]);
	string package_name(argv[2]);
	string page_name(argv[3]);
	string if_gen_stdfunc_str(argv[4]);
	string ofile(argv[5]);

	bool if_gen_stdfunc;
	if (if_gen_stdfunc_str == "false")if_gen_stdfunc = false;
	else if (if_gen_stdfunc_str == "true")if_gen_stdfunc = true;
	else exit(-1);
	if (package_name == "null")package_name = "";
	if (page_name == "null")page_name = "";

	Widget_Collection::init();
	Page page(package_name.c_str(), page_name.c_str(), if_gen_stdfunc);
	XmlParser p(ifile.c_str());
	p.bind_page(&page);
	p.parse2Page();
	page.save(ofile.c_str());
	return 0;
}