#include "Widget_Collection.h"

vector<Widget> Widget_Collection::_widgets = vector<Widget>();

Widget_Collection::Widget_Collection()
{
}

void Widget_Collection::init() {
	ifstream inFile;
	inFile.open("widget_collection.csv", ios::in);
	if (inFile) {
		string line;
		queue<vector<string>> vec_q;
		while (getline(inFile, line)) {
			vector<string> split_line_vec;
			SplitString(line, split_line_vec, ",");
			vec_q.push(split_line_vec);
		}

		init_widgets(vec_q);
		//inFile.close();
		//ofstream of;
		//of.open("widget_collection.dat",ofstream::binary);
		//for (int i = 0; i < _widgets.size(); ++i) {
		//	of << _widgets[i].name << endl << _widgets[i].import_package << endl << _widgets[i].func_name << endl;
		//}
		//of.close();
	}
	else {
		cout << "error:data file does not exist!";
		exit(-1);
	}

}

void Widget_Collection::SplitString(const string& s, vector<string>& v, const string& c) {
	std::string::size_type pos1, pos2;
	pos2 = s.find(c);
	pos1 = 0;
	while (std::string::npos != pos2)
	{
		v.push_back(s.substr(pos1, pos2 - pos1));
		pos1 = pos2 + c.size();
		pos2 = s.find(c, pos1);
	}
	if (pos1 == s.length()) v.push_back("");
	else v.push_back(s.substr(pos1));
}


void Widget_Collection::init_widgets(queue<vector<string>> vec_q) {
	while (!vec_q.empty()) {
		vector<string> split_line_vec = vec_q.front();
		_widgets.push_back(Widget{ split_line_vec[0], split_line_vec[1], split_line_vec[2] });
		vec_q.pop();
	}
}

Widget Widget_Collection::get_widget_byId(int id) {
	return _widgets[id];
}

Widget Widget_Collection::get_widget_byName(const char* name) {
	for (int i = 0; i < _widgets.size(); ++i) {
		Widget temp = _widgets[i];
		if (temp.name == name)return temp;
	}
	cout << "error:can't find widget type " << name << endl;
	exit(-1);
}

int Widget_Collection::get_widgetId_byName(const char* name) {
	for (int i = 0; i < _widgets.size(); ++i) {
		Widget temp = _widgets[i];
		if (temp.name == name)return i;
	}
	return -1;
}

string Widget_Collection::get_widgetName_byId(int id) {
	return _widgets[id].name;
}

int Widget_Collection::getLen() {
	return _widgets.size();
}
