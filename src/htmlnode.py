class HTMLNODE:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children if children else []
        self.props = props or {}

    def to_html(self):
        raise NotImplementedError("Not Implemented")
    
    def props_to_html(self):
        output = ""
        for attribute in self.props:
            output += f' {attribute}="{self.props[attribute]}"'
        return output
    
    def __repr__(self):
        if not self.children and not self.props:
            return f'tag = {self.tag}\nvalue = {self.value}'

        if not self.children:
            return f'tag = {self.tag}\nvalue = {self.value}\nprops = {self.props}'
        
        else:

            return f'tag = {self.tag}\nvalue = {self.value}\nchildren = {self.children}\nprops = {self.props}'




class LeafNode(HTMLNODE):
    def __init__(self, tag, value, props=None):
        super().__init__(tag,value,children = None, props=props)

    def to_html(self):
       if not self.value and self.tag != "img":
           raise ValueError("there is no Value")
       
       if not self.tag:
           return f"{self.value}"
       
       else:
           propshtml = self.props_to_html()
           return f"<{self.tag}{propshtml}>{self.value}</{self.tag}>"
       
       

class ParentNode(HTMLNODE):
    def __init__(self, tag,children,props=None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        
        if not self.tag:
           raise ValueError("there is no Tag")
       
        if not self.children:
           raise ValueError("there are no Children")
    
        result = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            result+= child.to_html()    
        result+= f"</{self.tag}>"
        return result
    

       

