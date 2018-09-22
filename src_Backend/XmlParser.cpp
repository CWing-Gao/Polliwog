#include "XmlParser.h"

XmlParser::XmlParser(const char* filename) {
	_filename = filename;
	_init = 0;
}

void XmlParser::set_filename(const char* filename) {
	_filename = filename;
}

void XmlParser::bind_page(Page* bindpage) {
	_bind_page = bindpage;
	_exist_record = bindpage->get_exist_record_pointer();
	_ids = bindpage->get_ids_pointer();
}

void XmlParser::load_file() {
	_doc = TiXmlDocument(_filename.c_str());
	if (!_doc.LoadFile()) {
		cout << "Error: Failed to load xml file!\n";
		exit(-1);
	}
}

void XmlParser::parse2Page() {
	if (!_init) {
		load_file();
		_init = 1;
	}
	TiXmlElement *rootElement = _doc.RootElement();
	traverse(rootElement);
	import2page();
	func2page();
}

void XmlParser::traverse(TiXmlElement* element) {
	for (TiXmlElement* ele_i = element; ele_i != NULL; ele_i = ele_i->NextSiblingElement()) {
		const char* v = ele_i->Value();
		if (v) {
			int index = Widget_Collection::get_widgetId_byName(v);
			if (index != -1) {
				record_exist(index);
				const char* id_c = ele_i->Attribute("android:id");
				if (id_c) {
					string id(id_c);
					id = string(id).substr(5, id.length() - 5);
					record_ids(index, id.c_str());
				}
			}
		}
		TiXmlElement* firstChild = ele_i->FirstChildElement();
		if (firstChild)traverse(firstChild);
	}
}

void XmlParser::record_exist(int index) {
	_exist_record[index] = true;
}

void XmlParser::record_ids(int index, const char* id) {
	if (index != -1)_ids[index].push(id);
}

string XmlParser::gen_import() {
	string import_data = "";
	for (int i = 0; i < Widget_Collection::getLen(); ++i) {
		if (_exist_record[i]) {
			Widget temp = Widget_Collection::get_widget_byId(i);
			if (temp.import_package != "")import_data = import_data + "import " + temp.import_package + "\n";
		}
	}
	return import_data;
}

void XmlParser::import2page() {
	_bind_page->set_extra_import(gen_import());
}

void XmlParser::func2page() {
	for (int i = 0; i < Widget_Collection::getLen(); ++i) {
		if (_exist_record[i]) {
			Widget temp = Widget_Collection::get_widget_byId(i);
			if (temp.func_name != "")_bind_page->add_func(temp.func_name.c_str());
		}
	}
}