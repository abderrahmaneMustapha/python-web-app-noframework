def render(path):
    with open(path, "r") as f:
        template= f.read() 
        return  template.encode("utf-8")
