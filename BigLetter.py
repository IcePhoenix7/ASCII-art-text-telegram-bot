class BigLetter: 
    def __init__(self,letter,letter_view) -> None:
        self.letter = letter
        self.letter_display = letter_view 
    
    def get_line(letter_view,line_number):#re do it
        line = ""
        current_line_number = 0
        for ch in letter_view:
            if ch == "\n":
                if current_line_number == line_number:
                    break
                else:
                    current_line_number+=1
                    line = ""
            else:
                line+=ch
        return line

    def get_height(letter_view):
        height = 1
        for ch in letter_view:
            if ch =="\n":
                height+=1

        return height


    def add_letters(letter1,letter2):
        lines =""
        for h in range(max(get_height(letter1),get_height(letter2))): # make more understandable
            lines = lines + "\n" + get_line(letter1,h) + " " + get_line(letter2,h)
        return lines    

    def get_letter_len(letter):
        return len(get_line(letter,0))


