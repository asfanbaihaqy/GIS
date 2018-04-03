import mapnik

#MEMBUAT PETA
m = mapnik.Map(1080,720) #ukuran peta
m.background = mapnik.Color('white') #memberikan warna biru pada background peta

#MEMBUAT GAYA
s = mapnik.Style() #mendlakarasikan var "s" sebagai style/gaya
r = mapnik.Rule() #mendlakarasikan var "r" sebagai rule
#untuk membuat/mengisi "poligon" kita harus deklarasikan PolygonSymbolizer
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#D5F4F8')
r.symbols.append(polygon_symbolizer) #menambahkan "polygon_symbolizer" sebagai simbol di var "r"

#to add outlines to a polygon we create a LineSymbolizer
line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('red'),0.1) #on windows
#line_symbolizer.stroke = mapnik.Color('red') #on linux
#line_symbolizer.stroke_width = 0.1 #untuk windows tdk di pakai
r.symbols.append(line_symbolizer) #menambahkan "line_symbolizer" sebagai simbol di var "r"
s.rules.append(r) #mendlakarasikan var "r"  ke var "s" nb.style nya adalah var "r"
m.append_style('gaya1',s) #var "gaya1" adalah nama style map kamu

#MEMBUAT SUMBERDATA PETA 
ds = mapnik.Shapefile(file = "data shp/data1/ne_110m_admin_0_countries.shp") #nama sumber data map kamu di direktori misalnya "ne_110m_admin_0_countries.shp"

#MEMBUAT LAYER/LAPISAN
layer = mapnik.Layer('layout1') #deklarasi layout map kamu adalah var "peta1"
layer.datasource = ds #deklarasi var "ds" adalah sumber data dr layout map
layer.styles.append('gaya1')

#PERSIAPAN ME-RENDER MAP
m.layers.append(layer)
m.zoom_all()

#PROSES RENDER
mapnik.render_to_file(m,'peta1.pdf','pdf')
print"silahkan lihat hasilnya sob.."