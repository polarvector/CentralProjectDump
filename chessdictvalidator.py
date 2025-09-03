def isValidChessBoard(boardState):
    count = {}      
    for k,v in boardState.items():
        
        # Position validity loop
        i=0
        for character in k:
            if i%2==0:
                if int(character)>8:
                    print('L1S1')
                    return print('Pieces are positioned out of bounds!')
                
            if i%2==1:
                if type(character) != int and character > 'h':
                    print('L1S2')
                    return print('Pieces are positioned out of bounds!')
            i+=1

        # Pieces validity loop
        i=0
        for value in v:
            if i%2==0:
                if value not in ['w','b']:
                    print('L2S1')
                    return print('Invalid color!')
            
            if i%2==1:
                count.setdefault(value,0)
                count[value]=count[value]+1
                if value not in ['k','q','r','b','n','p']:
                    print('L2S2')
                    return print('Invalid piece!')
            i+=1

        for k,v in count.items():
            rule = {'k':1,'q':1,'r':2,'b':2,'n':2,'p':8}
            if v>rule[k]:
                return print('Too many pieces!')

    return print('Board state valid!')
