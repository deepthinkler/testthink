#include<QApplication>
#include<QWidget>
int main(int argc,char ** argv)
{
    QApplication app(argc,argv);
    QWidget* pWidget = new QWidget();
    pWidget->show();
    return app.exec();

}
