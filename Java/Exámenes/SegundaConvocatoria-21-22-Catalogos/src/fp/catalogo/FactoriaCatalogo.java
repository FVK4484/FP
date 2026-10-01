package fp.catalogo;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

import fp.utiles.Checkers;
import fp.utiles.Ficheros;

public class FactoriaCatalogo {
	
	private static Componente parsearComponente(String lineaCSV) {
		Checkers.checkNoNull(lineaCSV);
		String [] trozos = lineaCSV.split(",");
		Checkers.check("El número de trozos tiene que ser igual a 7.", trozos.length == 7);
		String nombre = trozos[0].trim();
		TipoComponente tipoComponente = TipoComponente.valueOf(trozos[1].trim());
		String suministrador = trozos[2].trim();
		Integer demora = Integer.valueOf(trozos[3].trim());
		Double precio = Double.valueOf(trozos[4].trim());
		Double descuento = Double.valueOf(trozos[5].trim());
		Set<String> combinadores = parsearCombinadores(trozos[6].trim());
		return new Componente(nombre, tipoComponente, suministrador, demora, precio, descuento, combinadores);
	}
	
	private static Set<String> parsearCombinadores(String combinadoresCSV) {
		String combinadoresNuevos = combinadoresCSV.replace("[", "").replace("]", "");
		Set<String> combinadores = new HashSet<>();
		for (String combinador : combinadoresNuevos.split(";")) {
			combinadores.add(combinador);
		}
		return combinadores;
	}

	public static Catalogo leerCatalogo(String rutaFichero) {
		Checkers.checkNoNull(rutaFichero);
		List<String> listaLineas = Ficheros.leeFichero("", rutaFichero);
		Set<Componente> componente = new HashSet<>();
		for (String linea : listaLineas) {
			componente.add(parsearComponente(linea));
		}
		return new Catalogo(componente);
 	}
	
}
