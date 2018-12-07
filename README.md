# K9    
A kanine info service

## How-to run
> docker-compose up app

Service will run on localhost's 80 port

## How to use

### Breeds of Dog API
Create breed with 
> POST /breed/
>
> {"name": "Akita"} 

Service will respond with created breed, automatically assigning it unique id 

Get breed by id
> GET /breed/id/

Update breed with specified fields
> PATCH /breed/id/
>
> {"name": "Akita-inu"}

Delete breed
> DELETE /breed/id/

If there are dogs of this breed, than service will respond with status 424

Get all breeds 
> GET /breeds/

### Dogs API
Create dog with 
> POST /dog/
>
> {"name": "Hachi-ko", "breed": "breed_id"}

Service will respond with created dog, automatically assigning it unique id 

Get dog by id
> GET /dog/id/

Update dog with specified fields
> PATCH /dog/id/
>
> {"breed": "new_breed_id"}

Delete dog
> DELETE /dog/id/

Get all dogs 
>GET /dogs/

Find dog by it's name 
> GET /dogs/?name=Hachi-ko

## Run tests
> docker-compose up test  
