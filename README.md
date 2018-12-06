# K9    
A kanine info service

## How-to run
> docker-compose up app

Service will run on localhost's 80 port

## How to use

### Breeds of Dog service
Create breed with 
> POST /breed/
>
> {name: "Akita"} 

Service will respond with created breed, automatically assigning it unique id 

Get breed by id
> GET /breed/id/

Update breed with specified fields
> PATCH /breed/id/
>
> {name: "Akita-inu"}

To delete breed
> DELETE /breed/id/

If there are dogs of this breed, than service will respond with status 424

To get all breeds 
> GET /breeds/

### Dogs service
Create dog with 
> POST /dog/
>
> {name: "Hachi-ko", breed: "breed_id"}

Service will respond with created dog, automatically assigning it unique id 

Get dog by id
> GET /dog/id/

Update dog with specified fields
> PATCH /dog/id/
>
> {breed: "new_breed_id"}

To delete dog
> DELETE /dog/id/

To get all dogs 
>GET /dogs/

To find dog by it's name 
> GET /dogs/?name=Hachi-ko

## Run tests
> docker-compose up test  
