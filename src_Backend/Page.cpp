#include "Page.h"

using namespace std;

// provided for check and debug
//void Page::print_button() {
//	queue<string> button_copy = _buttons;
//	while (!button_copy.empty()) {
//		cout << button_copy.front() << endl;
//		button_copy.pop();
//	}
//}

Page::Page(const char* package_name = "PACKAGE_NAME_PLACEHOLD", 
	const char* page_name = "PAGE_NAME_PLACEHOLD",
	bool if_gen_stdfunc = false)
{
	_if_gen_stdfunc = if_gen_stdfunc;
	string page_name_str, package_name_str;
	page_name_str = string(page_name);
	package_name_str = string(package_name);
	_page_name = (page_name_str == "" ? "PAGE_NAME_PLACEHOLD" : page_name);
	_package_name = (package_name_str == "" ? "PACKAGE_NAME_PLACEHOLD" : package_name);

	int widget_collection_len = Widget_Collection::getLen();
	_exist_record = new bool[widget_collection_len] {false};
	_ids = new queue<string>[widget_collection_len];

	init_fixed_info();
}

bool* Page::get_exist_record_pointer() {
	return _exist_record;
}

queue<string>* Page::get_ids_pointer() {
	return _ids;
}

void Page::init_fixed_info() {
	_basic_import = "import android.os.Handler;\nimport android.os.Message;\nimport android.support.v7.app.ActionBar;\nimport android.support.v7.app.AppCompatActivity;\n\n";

	_activity_prefix = "public class PageName implements View.OnClickListener, {\n\tAppCompatActivity parent=null;\n\tMainActivity.MainHandler mainHandler=null;\n\n";

	_activity_postfix = "\tvoid memoryClear(){\n\t}\n\t@Override\n\tpublic void onClose(){\n\t\treturn false;\n\t}\n}";

	_activity_PageGet = "\tpublic PageGet(AppCompatActivity parent, Handler mainHandler){\n\t\tthis.parent= parent;\n\t\tthis.mainHandler=( MainActivity.MainHandler)mainHandler;\n\t}\n\n";

	_activity_SetUI = "\tpublic void setUI() {\n\t\tparent.setContentView(R.layout." + _page_name + ");\n\t\tActionBar actionBar = parent.getSupportActionBar();\n\t\tactionBar.hide();\n\t}\n\n";
}

void Page::set_page_name(const char* page_name) {
	_page_name = page_name;
}

void Page::set_package_name(const char* package_name) {
	_package_name = package_name;
}

void Page::add_func(const char* func) {
	_functions.push(func);
}

void Page::save(const char* target) {
	gen_data();
	ofstream of;
	of.open(target);
	of << _data;
	cout << "successfully output data to " << string(target);
	of.close();
}

void Page::gen_data() {
	put_package_name();
	put_import();
	put_activity();
}

void Page::put_package_name() {
	_data = _data + "package " + _package_name + ";\n\n";
}

void Page::put_import() {
	_data = _data + _basic_import + _extra_import + "\n";
}

void Page::put_activity() {
	put_activity_prefix();
	put_activity_content();
	put_activity_postfix();
}

void Page::put_activity_prefix() {
	_data += _activity_prefix;
}

void Page::put_activity_postfix() {
	_data += _activity_postfix;
}

void Page::put_activity_content() {
	put_activity__widget_declaration();
	put_activity__PageGet();
	put_activity__setUI();
	put_activity__loadControl();
	if (_if_gen_stdfunc)put_activity__widget_function();
}

void Page::put_activity__widget_declaration() {
	for (int i = 0; i < Widget_Collection::getLen(); ++i) {
		if (!_ids[i].empty()) {
			string widget_name = Widget_Collection::get_widgetName_byId(i);
			queue<string> ids_copy = _ids[i];
			while (!ids_copy.empty()) {
				_data = _data + "\tprivate " + widget_name + " " + ids_copy.front() + "=null\n";
				ids_copy.pop();
			}
		}
	}
	_data += "\n";
}

void Page::put_activity__PageGet() {
	_data += _activity_PageGet;
}

void Page::put_activity__setUI() {
	_data += _activity_SetUI;
}

void Page::put_activity__loadControl() {
	_data += "\tpublic void loadControl() {\n";
	for (int i = 0; i < Widget_Collection::getLen(); ++i) {
		if (!_ids[i].empty()) {
			string widget_name = Widget_Collection::get_widgetName_byId(i);
			queue<string> ids_copy = _ids[i];
			while (!ids_copy.empty()) {
				_data = _data + "\t\t" + ids_copy.front() +
					"=(" + widget_name + ") parent.findViewById(R.id." + ids_copy.front() + ");\n";
				ids_copy.pop();
			}
		}
	}
	_data += "\t}\n\n";
}

void Page::put_activity__widget_function() {
	queue<string> func_copy = _functions;
	while (!func_copy.empty()) {
		string func_name = func_copy.front();
		_data += "\t@Override\n\tpublic void " + func_name + " {\n";
		gen_func_content(func_name);
		_data += "\t}\n\n";
		func_copy.pop();
	}
}

void Page::gen_func_content(string func_name) {
	if (func_name == "onClick(View v)")put_activity__onClick();
}

void Page::put_activity__onClick() {
	_data += "\t\tMessage msg=new Message();\n\t\tswitch (view.getId()){\n";

	queue<string>button_copy = _ids[Widget_Collection::get_widgetId_byName("Button")];
	while (!button_copy.empty()) {
		_data = _data + "\t\t\tcase R.id." + button_copy.front() + ":\n\t\t\t\tbreak;\n";
		button_copy.pop();
	}

	_data += "\t\t}\n";
}

void Page::set_extra_import(string import_data) {
	_extra_import = import_data;
}