# method: trim
# Trim the text
# @input, str: The input string
# @return, str: The output string
# @completed
import codecs

file = codecs.open("deneme3.txt", "w", "utf-8")
input = codecs.open("deneme.txt", encoding='utf-8')

def trim( input ):
        
        input = re.sub( r" +", " ", input )
        return input.strip()

        print(input)

file.write(input)
