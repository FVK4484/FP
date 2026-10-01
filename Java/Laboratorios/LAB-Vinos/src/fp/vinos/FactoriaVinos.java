package fp.vinos;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

import fp.utiles.Checkers;

public class FactoriaVinos {
	
	private static Vino parsearVino(String lineaCSV) {
		
		Checkers.checkNoNull(lineaCSV);
		String [] trozos = lineaCSV.split(",");
		Checkers.check("El Arry debe de tener 5 elementos.", trozos.length == 5);
		String pais = trozos[0].trim();
		String region = trozos[1].trim();
		Integer puntos = Integer.valueOf(trozos[2].trim());
		Double precio = Double.valueOf(trozos[3].trim());
		String uva = trozos[4].trim();
		return new Vino(pais, region, puntos, precio, uva);
	}
	
	private static List<String> leeLineas(String fichero) {
		List<String> result= new ArrayList<String>();
		try {
			result = Files.readAllLines(Path.of(fichero));
		} catch (IOException e) {
			e.printStackTrace();
		}
		return result;
	}
	
	public static List<Vino> leeVinos(String ficheroCSV) {
		Checkers.checkNoNull(ficheroCSV);
		List<Vino> listaVinos = new ArrayList<Vino>();
		List<String> lineas = leeLineas(ficheroCSV);
		lineas.remove(0);
		for(String linea : lineas) {
			listaVinos.add(parsearVino(linea));
		}
		return listaVinos;
	}
	
	public static Vinoteca leerVinotecaBucles(String ficheroCSV) {
		List<Vino> vinos = leeVinos(ficheroCSV);
		return new VinotecaBucles(vinos);
	}
	
	public static Vinoteca leerVinotecaStreams(String ficheroCSV) {
		List<Vino> vinos = leeVinos(ficheroCSV);
		return new VinotecaStream(vinos);
	}
	
}
