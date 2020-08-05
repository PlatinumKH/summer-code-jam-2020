def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'gallery/detail.html', {'album': album})