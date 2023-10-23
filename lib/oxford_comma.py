def oxford_comma(elements):
     if len(elements) == 1 :
          return elements[0]
     elif len(elements) == 2: 
          return " and ".join(elements)
     else:
          return ", ".join(elements[:-1]) + ", and " + elements[-1]




     #+ ", and " + (elements[-1])
  