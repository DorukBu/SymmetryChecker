## TODO:
## -README file
## -comment content and comment hierarchy check
##


from itertools import product

def symmchecker(stringParam):     ## wildcards parameter can be implemented w/ args kwargs 

  ifeven = True
  wildcard = '?'
  sngwcardindex = []
  dblwcardindex = []
  midindex = len(stringParam)//2
  letterlist = list(stringParam)
  letterset = set(letterlist)
  if wildcard in letterset:
    letterset.remove(wildcard)
  symmetry = True
  message = ''
  combilist = []
  finalcombilist = []
  imputationresult = ''
  finalcombiresult = ''
  combicount = 0
  
  ### Evenness Checker
  if (len(stringParam)%2) == 1:
    ifeven = False
  else:
    ifeven = True 

  ### Wildcard Index Finder
  for i in range(len(letterlist)):
    if (letterlist[i] == wildcard) & (i < midindex) & (letterlist[-i-1] == letterlist[i]):    ##check for symmetrical wildcards
      dblwcardindex.append(i)
    elif (letterlist[i] == wildcard) & (letterlist[-i-1] != letterlist[i]):   ## find the index of non-symmetrical wildcards !!! mid character disregarded !!!
      sngwcardindex.append(i)
    else:
      pass

  ### Check for symmetry with respect to wildcards
  for i in range(midindex):
    if letterlist[i] == letterlist[-i-1]:
      pass
    elif (letterlist[i] != letterlist[-i-1]) and (letterlist[i] != wildcard and letterlist[-i-1] != wildcard):
      symmetry = False


  ### Check for possible wildcard combinations if there are symmetrical (double) wildcards or a wildcard in the middle of an odd string. 
  ## Create a list of lists. Each sub-list is a possible wildcard imputation combination. !just one side of the symmetry!
  if (len(dblwcardindex) != 0) or (ifeven == False and letterlist[midindex] == wildcard):

    if (ifeven == False and letterlist[midindex] == wildcard):
      combilist = list(product(letterset, repeat = len(dblwcardindex)+1))
      dblwcardindex.append(midindex)
    else:
      combilist = list(product(letterset, repeat = len(dblwcardindex)))
  else:
    message = 'Error: Case escape #1'

  #### Print appropriate message -> symmetrical or not (w/ or w/out the help of wildcards) & possible combinations if any

  ### The string is not symmetrical w/ or w/out wildcards
  if symmetry == False:
    if (len(sngwcardindex) == 0) and (len(dblwcardindex) == 0):
      message = 'The string "{givenstring}" is not symmetrical and does not contain any wildcard(s).'
    else:
      message = 'The string "{givenstring}" is not symmetrical even with the wildcard(s).'

  #### The string is symmetrical w/ or w/out wildcards
  elif symmetry == True:
    ### there are no wildcards in the string and the string is symmetrical
    if (len(sngwcardindex) == 0) & (len(dblwcardindex) == 0):
      message = 'The string "{givenstring}" is symmetrical without the help of any wildcard.'

    ### there are only non-symmetrical wildcards and the string is symmetrical thanks to them. Convert wildcard values to mirroring letters.
    elif (len(sngwcardindex) != 0):
      for i in sngwcardindex:
        letterlist[i] = letterlist[-i-1]
      if len(dblwcardindex) == 0:
        imputationresult = ''.join(letterlist)      
        message = 'The string "{givenstring}" is symmetrical with the help of wildcard(s).\nThe string after the wildcard imputation is: {strwithimputation}'
      
    ### There are symmetrical (double) wildcards or a sinle wildcard in the middle of the string. 
    ### Generate message containing wildcard imputation combinations using letters present in the given string (letterset)
    elif len(dblwcardindex) != 0 and len(letterlist) != 1:

      u = 0
      while u<len(dblwcardindex):
        for i in combilist :
          t=0
          templist1 = letterlist.copy()
          while t<len(dblwcardindex):
            for j in dblwcardindex:
              templist1[j] = combilist[u][t]
              templist1[-j-1] = combilist[u][t]
              t = t+1
            u = u +1
          finalcombilist.append(templist1)

      templist2 = []
      combicount = len(combilist)
      for i in finalcombilist:
        tempstring = ''.join(i)
        templist2.append('\n' + tempstring)
        finalcombiresult = ''.join(templist2)
      message = 'The string "{givenstring}" is symmetrical and contains symmetrical wildcard(s).\nThere are {count} possible imputation combinations using the letters present in the string. All listed below:\n{strwithalcombis}'
    else:
      message = 'Ha ha!'
  else:
    message = 'Error: Case escape #3'

  ### Print message
  print(message.format(givenstring = stringParam, strwithimputation = imputationresult, strwithalcombis = finalcombiresult, count = combicount))
