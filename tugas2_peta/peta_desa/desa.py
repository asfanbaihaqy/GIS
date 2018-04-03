import mapnik
m = mapnik.Map(800,300)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()

polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#6c3626')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('rgb(102,205,0)')
line_symbolizer.stroke_width = 0.1
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('my style',s)
ds = mapnik.Shapefile(file="Indo_Desa_region.shp")
layer = mapnik.Layer('desa')
layer.datasource = ds
layer.styles.append('my style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'desa.jpeg','jpeg')
print "rendered image to 'desa.jpeg'"
