from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


def index(request):
    # contatos = Contato.objects.all()  # SELECT * FROM contato

    # puxar todos e ordenar, o '-' é ordem decrescente
    contatos = Contato.objects.order_by('-id').filter(mostrar=True)
    paginator = Paginator(contatos, 3)

    page_number = request.GET.get('p')
    contatos = paginator.get_page(page_number)

    return render(request, 'contatos/index.html', {'contatos': contatos})


def ver_contato(request, contato_id):
    # contato = Contato.objects.get(id=contato_id)  # seleciona um único item
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404()

    return render(request, 'contatos/ver_contato.html', {'contato': contato})


def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        print('ENTROU')
        messages.add_message(
            request, messages.ERROR, 'Campo termo não pode ficar vazio.'
        )
        return redirect('index')
        # raise Http404()

    campos = Concat('nome', Value(' '), 'sobrenome')

    contatos = Contato.objects.annotate(nome_completo=campos).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )

    '''
    contatos = Contato.objects.order_by('-id').filter(
        # Q 'monta a query', para visualiza-la print(contatos.query)
        Q(nome__icontains=termo) | Q(sobrenome__icontains=termo),
        mostrar=True,
    )
    '''

    paginator = Paginator(contatos, 3)

    page_number = request.GET.get('p')
    contatos = paginator.get_page(page_number)

    return render(request, 'contatos/busca.html', {'contatos': contatos})
