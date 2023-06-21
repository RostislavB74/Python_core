unit Unit1;

 

interface

 

uses

  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,

  Dialogs, OpenGL, ExtCtrls, Math;

 

type

  TForm1 = class(TForm)

    Timer1: TTimer;

    procedure SetDCPixelFormat (hdc: HDC);

    procedure FormCreate(Sender: TObject);

    procedure FormPaint(Sender: TObject);

    procedure frac(x1,y1,x2,y2:double; deep:byte; inv:Shortint);

  private

    hrc: HGLRC;

    DC:HDC;

  public

    { Public declarations }

  end;

 

var

  Form1: TForm1;

  left_f:boolean;

  l,r:double;

  deep:byte;

  inv:Shortint;

 

implementation

 

{$R *.dfm}

 

procedure TForm1.SetDCPixelFormat (hdc: HDC);

var

  pfd: TPixelFormatDescriptor;

  nPixelFormat: Integer;

begin

  FillChar (pfd, SizeOf (pfd), 0);

  nPixelFormat:= ChoosePixelFormat (hdc, @pfd);

  SetPixelFormat (hdc, nPixelFormat, @pfd);

end;

 

procedure TForm1.FormCreate(Sender: TObject);

begin

  DC:=GetDC(Handle);

  SetDCPixelFormat(DC);

  hrc:=wglCreateContext(DC);

  wglMakeCurrent(DC, hrc);

  left_f:=true;

end;

 

procedure TForm1.FormPaint(Sender: TObject);

var

  x1,x2,y1,y2,x3,y3,x4,y4:double;

begin

  glClearColor(0,0,0,0);

  glColor3f (1,1,0);

  glClear (GL_COLOR_BUFFER_BIT);

  glPointSize(0.1);

  glLineWidth(1);

 

 

 

 

  //  координаты треугольника

  x1:=-0.8;

  y1:=-0.5;

  x2:=0;

  y2:=0.9;

  x3:=0.8;

  y3:=-0.5;

 

  glBegin(GL_LINE_STRIP); // рисуем начальную фигуру

    glVertex2d(x1,y1);

    glVertex2d(x2,y2);

    glVertex2d(x3,y3);

    glVertex2d(x1,y1);

  glEnd();

 

  deep:=7;

  inv:=-1;

  frac(x1,y1,x2,y2,deep,inv);

  frac(x2,y2,x3,y3,deep,inv);

  frac(x3,y3,x1,y1,deep,inv);

 

  SwapBuffers(DC);

  wglMakeCurrent (0, 0);

end;

 

procedure TForm1.frac(x1,y1,x2,y2:double; deep:byte; inv:Shortint);

var

  L,H,x1_osn,x2_osn,y1_osn,y2_osn,x_new,y_new:double;

  i:byte;

begin

  deep:=deep-1;

  if deep>1 then

  begin

  L:=sqrt(power((x1-x2),2)+power((y1-y2),2)); //  длинна основания

  x1_osn:=x1+(x2-x1)/3; // вычисляем кооординаты основания треугольника

  x2_osn:=x1_osn+(x2-x1)/3;

  y1_osn:=y1+(y2-y1)/3;

  y2_osn:=y1_osn+(y2-y1)/3;

  H:=L/(2*sqrt(3)); // высота нового равностороннего треугольника

  x_new:=(x2+x1)/2+H*(inv)*(y2-y1)/L; // координаты вершини треугольника

  y_new:=(y2+y1)/2-H*(inv)*(x2-x1)/L;

 

  glBegin(GL_LINE_STRIP); // закрашиваем основание треугольнкика

    glColor3f(0,0,0); // ____________________________________________________________

    glVertex2d(x1_osn,y1_osn);

    glVertex2d(x2_osn,y2_osn);

  glEnd();

 

  glBegin(GL_LINE_STRIP); // рисуем ребра треугольника

    glColor3f(0+1/H,1,0+1/y_new);

    glVertex 2d(x 1_osn,y 1_osn);

    glColor3f(1,0+1/x_new,0+1/y_new);

    glVertex2d(x_new,y_new);

    glColor3f(0+1/L,0+1/L,1);

    glVertex2d(x 2_osn,y 2_osn);

  glEnd();

 

  deep:=deep+1;

  l:=sqrt(sqr(x1_osn-x_new)+sqr(y1_osn-y_new));

  r:=sqrt(sqr(x2_osn-x_new)+sqr(y2_osn-y_new));

 

  frac(x 1_osn,y 1_osn,x_new,y_new,deep-1,inv);

  frac(x_new,y_new,x 2_osn,y2_osn,deep-1,inv);

  frac(x1,y1,x 1_osn,y1_osn,deep-1,inv);

  frac(x 2_osn,y 2_osn,x 2,y 2,deep-1,inv);

 

 

 

  end;

end;

 

end.