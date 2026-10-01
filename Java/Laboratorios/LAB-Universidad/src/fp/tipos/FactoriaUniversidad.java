package fp.tipos;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import fp.utiles.Checkers;

public class FactoriaUniversidad {
	
	public static List<Espacio> leeEspacios(String ruta) {
		List<Espacio> result = new ArrayList<Espacio>();
		try {
			List<String> lineas = Files.readAllLines(Paths.get(ruta));
			for (String linea : lineas) {
				result.add(parsearEspacio(linea));
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		return result;
	}
	
	public static Espacio parsearEspacio(String StrEspacio) {
		String[] trozos = StrEspacio.split(",");
		Checkers.check("Un espacio tiene 4 .", trozos.length == 4);
		String nombre = trozos[0].strip();
		Integer planta = Integer.valueOf(trozos[1].strip());
		Integer capacidad = Integer.valueOf(trozos[2].strip());
		TipoEspacio tipoEspacio = TipoEspacio.valueOf(trozos[3].strip().toUpperCase());
		return new Espacio(tipoEspacio, nombre, capacidad, planta);		
	}
}