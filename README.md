# Zipf-Toolkit

A statistical toolkit used to analyze frequency of words and test the "Zipfianess" of a corpus using techniques described in Clauset et. al. (Clauset, 2009). Package includes ability to tokenize, parse, generate frequency table, generate rank vs frequency log-log plots, generate p-value to determine if distribution follows a power-law, and compare fit of distribution to poisson, exponential, and log-normal distributions. 

To do so we used:
    -The Python programming language (python.org) and matplotlib (matplotib.org) to tokenizesome of the written corpora and to do the rank/frequency plots 
    -The R Project for Statistical Computing (r-project.org) to encode the techniques.


The following are instructions to setup and run the project.

To setup the directory for the project do the following steps as necessary: 

  Install the necessary languages:
    -Python
    -R
  
  Install pip:
    -https://pip.pypa.io/en/stable/installing/
    
  In repository directory run the command to install the necessary python packages:
    $ make setup
    
  In repository create a R shell and install the "poweRlaw" package using the following commands and continue by following the package directions:
    $ R
    > install.packages('poweRlaw')
    
    
To run an example to generate a fequency csv file from a portion of the Brown corpus (Francis, 1970) input the following code in the terminal:
    make example

To generate statstical analysis of distribution do the following:
    enter R environment by entering 'R' into termninal.
    enter the folliwng command:
    
      > source('getInfo.R')
    
    follow input instructions:
      
      Input name of file containing frequency table seperated by ','
      
      Input what you would like the output file name to be.
    
    The output file will contain statistical analysis of frequency distribution.
      
Other commands in terminal:
    Create a frequency vs rank log-log plot given a file containing a words and frequencies:
       $ make create
    
    Tokenized a text file using nltk and create a csv file containing words and given frequencies:
       $ make csv
    
  References:
    Clauset, A., Shalizi, C. R., Newman, M. E. J. (2009). Power-law distributions in empirical data.SIAM review, 51(4), 661–703. doi:10.1137/070710111.
    
    Francis, W. N., Kucera, H. (1979). \emph{Brown corpus manual: manual of information to accompany a standard corpus of present-day edited American English for   use with digital computers}. Providence: Brown University.
    
