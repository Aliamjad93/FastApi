from Route import routes

import uvicorn



if __name__=='__main__':
    
    uvicorn.run(routes.Rout.app,host="127.0.0.1",port=8000)