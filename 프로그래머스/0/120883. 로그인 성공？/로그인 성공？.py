def solution(id_pw, db):
    
    w_dirty = 0
    
    for i in range(len(db)):
        if db[i][0] == id_pw[0]:
            if db[i][1] == id_pw[1]:
                return "login"
            else:
                w_dirty = 1

    if w_dirty == 1:
        return "wrong pw"
    else:
        return "fail"
