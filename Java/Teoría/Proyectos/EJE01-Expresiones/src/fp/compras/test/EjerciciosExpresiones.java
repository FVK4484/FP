package fp.compras.test;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

import fp.compras.Compra;

public class EjerciciosExpresiones {

	public static void main(String[] args) {
		
		Compra Compra1 = new Compra("40961226C", "Mercadona"
				, "Cádiz", LocalDateTime.of(2019, 2, 24, 5, 33)
				, LocalDateTime.of(2019, 2, 24, 5, 57), 8.65);
		Compra Compra2 = new Compra("86302030G", "Mercadona"
				, "Malaga", LocalDateTime.of(2019, 2, 24, 10, 1)
				, LocalDateTime.of(2019, 2, 24, 10, 34), 188.65);
		Compra Compra3 = new Compra("37089432T", "Mas"
				, "Granada", LocalDateTime.of(2019, 2, 24, 10, 9)
				, LocalDateTime.of(2019, 2, 24, 12, 56), 60.43);
		Compra Compra4 = new Compra("97785005E", "Mercadona"
				, "Malaga", LocalDateTime.of(2019, 2, 24, 13, 58)
				, LocalDateTime.of(2019, 2, 24, 15, 48), 17.43);
		
		System.out.println(
				Compra1.getProvincia().equals("Malaga") &&
				Compra1.getTotalCompra() > 60);
		
		LocalDateTime fechaTope = LocalDateTime.of(2019, 2, 28, 17, 35);
		System.out.println(Compra3.getFechaSalida().isBefore(fechaTope));
		
		
		System.out.println(Compra1.getSupermercado().equals("Mercadona") ||
				Compra1.getSupermercado().equals("Mercadona"));
		
		System.out.println(Compra2.getFechaSalida().getDayOfYear() == 
				Compra3.getFechaSalida().getDayOfYear());
		
		System.out.println(Compra2.getSupermercado().equals(Compra4.getSupermercado()) && 
				Compra2.getTotalCompra() > 100 || Compra4.getTotalCompra() > 100);
		
		System.out.println(Compra2.getTotalCompra() > 2 * Compra4.getTotalCompra());
		
		List<Compra> l1 = new ArrayList<>();
		l1.add(Compra1);
		l1.add(Compra2);
		
		Double suma = 0.0;
		for(int i = 0; i < l1.size(); i++) {
			suma += l1.get(i).getTotalCompra();
		}
		
		for (Compra c: l1) {
			suma += c.getTotalCompra();
		}
		Double media = suma / l1.size();
		
		System.out.println(media);
	
	}

}
