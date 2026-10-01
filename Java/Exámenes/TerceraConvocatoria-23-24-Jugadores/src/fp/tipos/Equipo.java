package fp.tipos;

import fp.utiles.Checkers;

public record Equipo(String nombre, Integer clasificacion, String estadio) {
	
	public Equipo {
		Checkers.check("La posición en la clasificación debe estar comprendida entre 1 y 20."
				, clasificacion >= 1 && clasificacion <= 20);
		Checkers.check("La propiedad estadio debe comenzar por la cadena “Estadio”."
				, estadio.startsWith("Estadio"));;
	}

}
