import mapnik

m = mapnik.Map(1080,720)
m.background = mapnik.Color('#93d4f5')

r = mapnik.Rule()
s = mapnik.Style()

ps = mapnik.PolygonSymbolizer()
ps.fill = mapnik.Color('white')
r.symbols.append(ps)

ls = mapnik.LineSymbolizer()
ls = mapnik.LineSymbolizer(mapnik.Color('#ff6779'),0.1)
r.symbols.append(ls)

ts = mapnik.TextSymbolizer(mapnik.Expression('[NAME]'),'DejaVu Sans Bold', 8 ,mapnik.Color('#2f2f30'))
r.symbols.append(ts)

s.rules.append(r)
m.append_style('gaya',s)

ds = mapnik.Shapefile(file = "shp/ne_110m_admin_0_countries.shp")

layer = mapnik.Layer('output')
layer.datasource = ds
layer.styles.append('gaya')

m.layers.append(layer)
m.zoom_all()

#layer 2
r = mapnik.Rule()
s = mapnik.Style()

ls2 = mapnik.LineSymbolizer()
ls2 = mapnik.LineSymbolizer(mapnik.Color('yellow'),2)
r.symbols.append(ls2)

ts2 = mapnik.TextSymbolizer(mapnik.Expression('[nama]'),'DejaVu Sans Bold', 8 , mapnik.Color('red'))
r.symbols.append(ts2)

s.rules.append(r)
m.append_style('gaya2',s)

ds = mapnik.Shapefile(file = "C:/Users/anu/Desktop/GIS/tugas/tugas6/qgis/main.shp")

layer = mapnik.Layer('output2')
layer.datasource = ds
layer.styles.append('gaya2')

m.layers.append(layer)
m.zoom_all()

mapnik.render_to_file(m,'output.pdf','pdf')
print"berhasil...."