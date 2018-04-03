import mapnik
m = mapnik.Map(600,300)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#66cd00')
r.symbols.append(polygon_symbolizer)
line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('#ffffff')
line_symbolizer.stroke_width = 0.1
r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('my style',s)
ds = mapnik.Shapefile(file="INDONESIA_KEC.shp")
layer = mapnik.Layer('kecamatan')
layer.datasource = ds
layer.styles.append('my style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'kecamatan.tif','tif')
print "rendered image to 'kecamatan.tif'"
