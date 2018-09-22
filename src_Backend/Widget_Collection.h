#pragma once
#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
using namespace std;

#ifndef WIDGET_COLLECTION_H
#define WIDGET_COLLECTION_H
typedef struct sWidget {
	string name;
	string import_package;
	string func_name;
}Widget;

class Widget_Collection
{
private:
	static vector<Widget>_widgets;
	static void SplitString(const std::string & s, std::vector<std::string>& v, const std::string & c);
	static void init_widgets(queue<vector<string>> vec_q);

public:
	Widget_Collection();
	static void init();
	static Widget get_widget_byId(int id);
	static Widget get_widget_byName(const char* name);
	static int get_widgetId_byName(const char * name);
	static string get_widgetName_byId(int id);
	static int getLen();
};

#endif