from conDB import Con
c = Con
class Action:
    def gethard_ware():
        data = c.getNamehard_ware()
        return data

    def gethard_ware():
        data = c.getNamehard_ware()
        return data

    def updatehard_ware(id,status,value):
        t = c.updatahard_ware(id, status,value)
        if(t == True):
            data = c.gethard_ware_ID(id)
        else:
            data = {"error": True}
        return data

    def inserthard_ware(name,hw_name):
        id = c.inserthard_ware(name,hw_name)
        if(id):
            data = c.gethard_ware_ID(id)
        else:
            data = {"error": True}
        return data