package fp.tipos.test;

import java.util.List;

import fp.tipos.FactoriaVuelos;
import fp.tipos.Vuelo;

public class TestFactoriaVuelos {

	public static void main(String[] args) {
		List<Vuelo> vuelos = FactoriaVuelos.leeVuelos("./data/aeropuerto.csv");
		for (Vuelo v : vuelos) {
			System.out.println(v);
		}
	}
	
}
