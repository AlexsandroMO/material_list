from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Produto, Tipo, Material, Altura, Largura, Caract, Bitola_PEC, Bitola_CAB, Tipo_Forn, Unidade
from .forms import ProdutoForm, AlturaForm #LdProjForm , SubjectForm, PageTypeForm, DocTypeForm, PageformatForm, DocumentModelForm, EmployeeForm, StatusDocForm, ActionForm #, LdProjForm, CotationForm
from django.contrib import messages

@login_required
def index(request):
    return render(request,'material/index.html')

@login_required
def create_material(request):
    return render(request,'material/create-material.html')


@login_required
def view_table(request):

    produtos = Produto.objects.all()
    tipos = Tipo.objects.all()
    materiais = Material.objects.all()
    alturas = Altura.objects.all()
    larguras = Largura.objects.all()
    caracts = Caract.objects.all()
    bitola_cabs = Bitola_PEC.objects.all()
    bitola_pecs = Bitola_CAB.objects.all()
    tipo_forns = Tipo_Forn.objects.all()
    unidades = Unidade.objects.all()
 
    #list_read = Produto.objects.filter(done='done', user=request.user).count()
    #produtos_filtrados = Produto.objects.filter(preco__gt=50)
    #tasks_list = Task.objects.all().order_by('-created_at').filter(user=request.user)

    return render(request, 'material/view-table.html', {'produtos':produtos,'tipos':tipos, 'materiais': materiais, 'alturas': alturas,
                                                        'larguras':larguras, 'caracts': caracts, 'bitola_cabs':bitola_cabs,
                                                        'bitola_pecs':bitola_pecs, 'tipo_fornss':tipo_forns, 'unidades':unidades})

@login_required
def new_action(request):
    if request.method == 'POST':
        form = AlturaForm(request.POST)
        
        if form.is_valid():
            altura = form.save(commit=False)
            altura.done = 'doing'
            altura.user = request.user
            altura.save()
            return redirect('/')
    else:
        form = AlturaForm()
        return render(request, 'material/addproduto.html', {'form': form})