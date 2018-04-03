import mapnik
m = mapnik.Map(700,350)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#ff9292')
r.symbols.append(polygon_symbolizer)
line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('rgb(60,50,50)')
line_symbolizer.stroke_width = 0.1
r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('my style',s)
ds = mapnik.Shapefile(file="INDONESIA_KAB.shp")
layer = mapnik.Layer('kabupaten')
layer.datasource = ds
layer.styles.append('my style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'kabupaten.png','png')
print "rendered image to 'kabupaten.png'"
