from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Produto
from .forms import ProdutoForm #LdProjForm , SubjectForm, PageTypeForm, DocTypeForm, PageformatForm, DocumentModelForm, EmployeeForm, StatusDocForm, ActionForm #, LdProjForm, CotationForm
from django.contrib import messages

@login_required
def index(request):
    return render(request,'material/index.html')

@login_required
def create_material(request):
    return render(request,'material/create-material.html')


@login_required
def view_table(request):
    return render(request,'material/view-table.html')

@login_required
def new_action(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        
        if form.is_valid():
            produto = form.save(commit=False)
            produto.done = 'doing'
            produto.user = request.user
            produto.save()
            return redirect('/')
    else:
        form = ProdutoForm()
        return render(request, 'material/addproduto.html', {'form': form})