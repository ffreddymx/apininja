from ninja import Router
from usuarios.models import Usuario
from usuarios.schemas import UsuarioSchema, UsuarioCreateSchema
from django.shortcuts import get_object_or_404

router = Router()

@router.get("/Usuario", response=list[UsuarioSchema])
def list_items(request):
    return list(Usuario.objects.all())


@router.get("/Usuario/{item_id}", response=UsuarioSchema)
def get_item(request, item_id: int):
    item = get_object_or_404(Usuario, id=item_id)
    return item


@router.post("/Usuario", response=UsuarioSchema)
def create_item(request, data: UsuarioCreateSchema):
    item = Usuario.objects.create(**data.dict())
    return item


@router.put("/Usuario/{item_id}", response=UsuarioSchema)
def update_item(request, item_id: int, data: UsuarioCreateSchema):
    item = get_object_or_404(Usuario, id=item_id)
    for attr, value in data.dict().items():
        setattr(item, attr, value)
    item.save()
    return item