package fp.tipos.test;

import java.util.ArrayList;
import java.util.List;

import fp.tipos.Espacio;
import fp.tipos.FactoriaUniversidad;
import fp.tipos.TipoEspacio;

public class TestEspacio {
	
	private static void muestraEspacios(List<Espacio> espacios) {
		for (Espacio espacio : espacios) {
			System.out.println(espacio);
		}
		
	}

	public static void main(String[] args) {
//		Espacio e = new Espacio(TipoEspacio.TEORIA, "A3.10", 70, 3);
//		System.out.println(e);
		
		//1. Lectura de ficheros
		List<Espacio> lineas = FactoriaUniversidad.leeEspacios("./data/espacios.csv");
		muestraEspacios(lineas);
	}

}
