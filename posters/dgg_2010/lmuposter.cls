%
%
\typeout{**********************************************}
\typeout{ Class: LMUPOSTER                             }
\typeout{ generation of A0 posters in portrait format  }
\typeout{ following LMU's corporate design guide       }
\typeout{ Lion Krischer, March 2010                    }
\typeout{ Derived from a landscape version made by     }
\typeout{ Marcus Mohr & Jens Oeser, March 2007         }
\typeout{ $Rev: 1 $                                    }
\typeout{**********************************************}
%
%

% =============================================================================
%  KENNDATEN
% =============================================================================
\ProvidesPackage{lmuposter}[2010/03/08]
\NeedsTeXFormat{LaTeX2e}

% =============================================================================
%  INITIALISIERUNGSTEIL
% =============================================================================

%
% Bools are required for the options part
%
\RequirePackage{ifthen}
\newboolean{PosterIsLandscape}
\setboolean{PosterIsLandscape}{true}

% =============================================================================
%  DEKLARATION VON OPTIONEN
% =============================================================================

%
% This option will re-set the colors to values which allow printing on a normal
% printer without wasting ink/toner for the background
%
\DeclareOption{portrait}{\setboolean{PosterIsLandscape}{false}}

% =============================================================================
%  AUSFUEHRUNG VON OPTIONEN
% =============================================================================
\ProcessOptions

% =============================================================================
%  LADEN VON PAKETEN
% =============================================================================

%
% This class is based on a0poster for A0 landscape posters
%
\LoadClass[portrait,a0]{a0poster}

%
% Use geometry package for setting page dimensions
%
\RequirePackage[paper=a0paper,portrait,left=44mm,right=44mm,top=44mm,%
headsep=0mm,headheight=0mm,centering]{geometry}

%
% We borrow fontsize definitions from the a0poster package
%
% !!!\LoadClass{article}
% !!!\input{a0size.sty}
% !!!\renewcommand{\tiny}{\fontsize{12}{14}\selectfont}
% !!!\renewcommand{\scriptsize}{\fontsize{14.4}{18}\selectfont}   
% !!!\renewcommand{\footnotesize}{\fontsize{17.28}{22}\selectfont}
% !!!\renewcommand{\small}{\fontsize{20.74}{25}\selectfont}
% !!!\renewcommand{\normalsize}{\fontsize{24.88}{30}\selectfont}
% !!!\renewcommand{\large}{\fontsize{29.86}{37}\selectfont}
% !!!\renewcommand{\Large}{\fontsize{35.83}{45}\selectfont}
% !!!\renewcommand{\LARGE}{\fontsize{43}{54}\selectfont}
% !!!\renewcommand{\huge}{\fontsize{51.6}{64}\selectfont}
% !!!\renewcommand{\Huge}{\fontsize{61.92}{77}\selectfont}
% !!!\newcommand{\veryHuge}{\fontsize{74.3}{93}\selectfont}
% !!!\newcommand{\VeryHuge}{\fontsize{89.16}{112}\selectfont}
% !!!\newcommand{\VERYHuge}{\fontsize{107}{134}\selectfont}
% !!!
% !!!\setlength\smallskipamount{6pt plus 2pt minus 2pt}
% !!!\setlength\medskipamount{12pt plus 4pt minus 4pt}
% !!!\setlength\bigskipamount{24pt plus 8pt minus 8pt}
% !!!
% !!!\setlength\abovecaptionskip{25pt}
% !!!\setlength\belowcaptionskip{0pt}
% !!!\setlength\abovedisplayskip{25pt plus 6pt minus 15 pt}
% !!!\setlength\abovedisplayshortskip{0pt plus 6pt}
% !!!\setlength\belowdisplayshortskip{13pt plus 7pt minus 6pt}
% !!!\setlength\belowdisplayskip\abovedisplayskip
% !!!
% !!!\normalsize


%
% Load additional required packages
%
\RequirePackage[pdftex]{color}
\RequirePackage[pdftex]{graphicx}
\RequirePackage{fancybox}

% =============================================================================
%  HAUPTTEIL
% =============================================================================

% ----------------
%  Define colours
% ----------------
\definecolor{white}{cmyk}{0.0,0.0,0.0,0.0}
\definecolor{lightGrayLMU}{cmyk}{0.0,0.0,0.0,0.25}
\definecolor{darkGrayLMU}{cmyk}{0.0,0.0,0.0,0.50}
\definecolor{greenLMU}{cmyk}{1.0,0.0,0.95,0.05}

% -----------------------------------------------------------------
%  Define and set defaults for height, width and distance of boxes
% -----------------------------------------------------------------
\newlength{\MyBoxHeight}
\newlength{\MyBoxWidth}
\newlength{\MyBoxHSep}
\newlength{\MyBoxVSep}
\newlength{\MyIntBoxSep}

\setlength{\MyBoxHSep}{10mm}
\setlength{\MyBoxVSep}{10mm}
%\setlength{\MyIntBoxSep}{2ex}
\setlength{\MyIntBoxSep}{8mm}

\setlength{\MyBoxHeight}{185mm}
\setlength{\MyBoxWidth}{355mm}

% Currently unnecessary I guess.
%\ifthenelse{\boolean{PosterIsLandscape}}{%
%\setlength{\MyBoxHeight}{185mm}
%\setlength{\MyBoxWidth}{341.9mm}
%}
%{
%\setlength{\MyBoxHeight}{185mm}
%\setlength{\MyBoxWidth}{343mm}
%}

% -------------------------------------
% Set background colour and page style
% -------------------------------------
\pagecolor{lightGrayLMU}
\pagestyle{empty}

%
% Define commands MyBox for visible and MyPseudoBox for invisible boxes
%
\newenvironment{MyAuxBox}[1]{\begin{minipage}[t]{0cm}\vspace{0pt}%
\rule{0cm}{#1}\end{minipage}%
\begin{minipage}[t]{\MyBoxWidth}\vspace{0pt}}{\end{minipage}}

\newcommand{\MyBox}[2][\MyBoxHeight]{\setlength{\fboxsep}{0pt}%
\shadowbox{\setlength{\fboxsep}{\MyIntBoxSep}\fcolorbox{white}{white}{%
\begin{MyAuxBox}{#1}#2\end{MyAuxBox}}}}

\newcommand{\MyPseudoBox}[2][\MyBoxHeight]{\color{lightGrayLMU}%
\setlength{\fboxsep}{0pt}\shadowbox{\setlength{\fboxsep}{2ex}%
\fcolorbox{lightGrayLMU}{lightGrayLMU}{\begin{MyAuxBox}{#1}#2\end{MyAuxBox}}}
\color{black}}

% ---------------------------
%  Define command PosterHead
% ---------------------------
\newcommand{\PosterHead}[1]{%
%
%
\noindent\setlength{\unitlength}{1mm}%
\begin{picture}(0,92)
%
% 1st box on the left (LMU logo a.k.a. 'Bildmarke')
%
\put(0,0){\makebox(92,92){\color{white}\rule{92mm}{92mm}}}
\put(0,6){\makebox(92,80)[b]{\includegraphics{LMU-logo-no-text-black}}}
\put(0,0){\framebox(92,92){\quad}}
%
% Central box (title, authors, etc.)
%
\put(102,0){\makebox(549,92)[b]{\color{white}\rule{549mm}{92mm}}}
\put(102,4){\makebox(549,88)[c]{\begin{minipage}[b]{547mm}\centering%
#1\end{minipage}}}
\put(102,0){\framebox(549,92){\quad}}
%
% Right box (MGC logo)
%
\put(661,0){\framebox(92,92){\color{white}\rule{92mm}{92mm}}}
\put(661,6){\makebox(92,80)[b]{\includegraphics{MGC-logo-english-450dpi}}}
%
% box on the right (cut LMU sigil)
%
%\put(906,0){\makebox(194,92){\color{white}\rule{194mm}{92mm}}}
%\put(906,0){\makebox(194,92)[br]{%
%\includegraphics[clip,viewport=0 50 390 450,height=92mm]%
%{LMU-Siegel-Schwarz50}}}
%\put(906,0){\framebox(194,92){}}
%
% Comment in for checking boundaries of poster
%
%\put(0,0){\line(0,-1){1101}}
%\put(753,0){\line(0,-1){1101}}
%\put(0,-1009){\line(1,0){1101}}
%
\end{picture}\\[24mm]}

% =============================================================================
%  EOF
% =============================================================================
