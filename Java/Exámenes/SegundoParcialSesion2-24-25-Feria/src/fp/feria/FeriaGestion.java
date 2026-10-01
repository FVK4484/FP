package fp.feria;

import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.SortedSet;
import java.util.TreeSet;
import java.util.function.Predicate;
import java.util.stream.Collectors;

public class FeriaGestion extends Feria {

	public FeriaGestion(Set<CasetaFeria> casetas) {
		super(casetas);
	}
	
	public String toString() {
		return super.toString() + "\n" + getCasetas().stream()
				.map(Object::toString)
				.collect(Collectors.joining("\n"));
	}
	
	// 1. getPrecioMaxProducto: Dado un tipo de caseta (pública o privada), devuelve un Map donde las claves 
	// son los nombres de los productos ofertados en casetas de ese tipo, y los valores el precio máximo registrado 
	// para ese producto en todas las casetas. Implemente este método con bucles. (1,5 ptos)	
	public Map<String, Double> getPrecioMaxProducto(TipoCaseta tipoCaseta) {
		Map<String, Double> dicc = new HashMap<>(); 
		for (CasetaFeria caseta : getCasetas()) {
			if (caseta.getTipoCaseta().equals(tipoCaseta)) {
				for (Producto producto : caseta.getMenu()) {
					String clave = producto.nombre();
					Double valor = producto.precio();
					if (!dicc.containsKey(clave) || 
							valor > dicc.get(clave)) {
						dicc.put(clave, valor);
					}
				}
			}
		}
		return dicc;
	}
	
	// 2. getValoracionMediaTipoCasetaAccesible: Dado un tipo de caseta (pública o privada) y un booleano que 
	// representa un valor de accesibilidad, devuelve la valoración media de todas las casetas de ese tipo que 
	// tengan el acceso adaptado según el valor indicado. Si no hay casetas que cumplan ambas condiciones, el método 
	// debe devolver 0.0. (1 pto)	
	public  Double getValoracionMediaTipoCasetaAccesible(TipoCaseta tipoCaseta, Boolean accesibilidad) {
		return getCasetas().stream()
				.filter(c -> c.getTipoCaseta().equals(tipoCaseta) && 
						c.getAccesoAdaptado().equals(accesibilidad))
				.collect(Collectors.averagingDouble(CasetaFeria::getValoracion));
	}
	
	// 3. getNombresProductos: Dado un umbral de precio, devuelve un conjunto ordenado alfabéticamente con los 
	// nombres de todos los productos cuyo precio sea inferior al umbral indicado. (1 pto)
	public SortedSet<String> getNombresProductos(Double umbral) {
		return getCasetas().stream()
				.flatMap(c -> c.getMenu().stream())
				.filter(c -> c.precio() < umbral)
				.map(c -> c.nombre())
				.collect(Collectors.toCollection(TreeSet::new));
	}
	
	// 4. getTopNCasetasPorMusica: Dado el nombre de un producto y un número entero n, devuelve un Map 
	// que asocie a cada tipo de música una lista con los nombres de las n casetas mejor valoradas que 
	// incluyan ese producto en su menú. (1,5 ptos)
	public Map<String, List<String>> getTopNCasetasPorMusica(String nombreProd, Integer n) {
		Predicate<CasetaFeria> pred = c -> c.getMenu().stream()
				.anyMatch(pr -> pr.nombre().equals(nombreProd));
		return getCasetas().stream()
				.filter(pred)
				.collect(Collectors.groupingBy(CasetaFeria::getMusica,
						Collectors.collectingAndThen(Collectors.toList(), 
								casetas -> getTopNCasetas(casetas, n))));			
				
	}
	
	private List<String> getTopNCasetas(List<CasetaFeria> casetas, Integer n) { 
		Comparator<CasetaFeria> cmp = Comparator.comparing(CasetaFeria::getValoracion); 
		return casetas.stream()
				.sorted(cmp.reversed())
				.limit(n)
				.map(CasetaFeria::getNombre)
				.collect(Collectors.toList()); 
	}

}
